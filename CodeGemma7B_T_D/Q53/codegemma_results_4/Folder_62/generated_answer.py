from collections import defaultdict

def palindrome_of_length_at_least_n(text):
    counts = defaultdict(int)
    for letter in text.lower():
        counts[letter] += 1
    result = set()
    for palindrome_len in range(31, len(text) + 1):
        for c1, c2 in counts.items():
            if c1 != c2:
                continue
            if palindrome_len % 2 == 0 and c1 * 2 < palindrome_len:
                continue
            if palindrome_len % 2 == 1 and c1 * 2 + 1 < palindrome_len:
                continue
            result.add(''.join([c1] * int(palindrome_len / 2)))
            result.add(''.join([c1] * int((palindrome_len - 1) / 2) + c2))
    return result