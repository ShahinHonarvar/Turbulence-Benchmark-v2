from collections import Counter

def palindromes_between_indices(s):
    sub_str = s[4:10]
    filtered = [c.lower() for c in sub_str if c.isalpha()]

    def is_palindrome_possible(counts, length):
        odd_count = sum((1 for count in counts.values() if count % 2 != 0))
        if length % 2 == 0:
            return odd_count == 0
        else:
            return odd_count <= 1
    if len(filtered) < 7 or not is_palindrome_possible(Counter(filtered), len(filtered)):
        return set()

    def create_palindrome(sorted_chars, path, counter, size, results):
        if len(path) == size // 2:
            mid = [] if size % 2 == 0 else [c for c in counter if counter[c] % 2][0]
            potential_palindrome = ''.join(path) + ''.join(mid) + ''.join(reversed(path))
            results.add(potential_palindrome)
            return
        for i in range(len(sorted_chars)):
            if counter[sorted_chars[i]] > 1:
                counter[sorted_chars[i]] -= 2
                path.append(sorted_chars[i])
                create_palindrome(sorted_chars, path, counter, size, results)
                path.pop()
                counter[sorted_chars[i]] += 2
    counts = Counter(filtered)
    sorted_chars = list(counts.keys())
    result_set = set()
    if is_palindrome_possible(counts, 7):
        create_palindrome(sorted_chars, [], counts.copy(), 7, result_set)
    return result_set