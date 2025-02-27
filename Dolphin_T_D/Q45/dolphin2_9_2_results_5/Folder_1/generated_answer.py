def palindromes_between_indices(s):
    substring = s[4:7]
    letters = [ch.lower() for ch in substring if ch.isalpha()]
    if len(letters) < 5:
        return set()
    length = len(letters)
    palindrome_set = set()
    for p in range(2, length + 1):
        for i in range(length - p + 1):
            s = letters[i:i + p]
            if len(set(s)) == 1:
                continue
            if s == s[::-1]:
                palindrome_set.add(''.join(s))
    return palindrome_set