def palindromes_between_indices(s):
    s = s[1:8].lower()
    letters = sorted((ch for ch in s if ch.isalpha()))
    result = set()

    def is_palindrome(seq):
        return seq == seq[::-1]

    def permute(path, counter):
        if len(path) >= 3 and is_palindrome(path):
            result.add(path)
        for i in range(len(counter)):
            if counter[i] > 0:
                counter[i] -= 1
                permute(path + letters[i], counter)
                counter[i] += 1
    unique_letters = sorted(set(letters))
    letter_count = [letters.count(c) for c in unique_letters]
    permute('', letter_count)
    return result