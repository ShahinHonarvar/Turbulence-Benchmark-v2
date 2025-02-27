def palindromes_between_indices(s):
    chars = [c.lower() for c in s[2:4] if c.isalpha()]
    if len(chars) < 2:
        return set()
    if len(chars) == 2:
        return set([''.join(chars), ''.join(reversed(chars))]) if chars[0] == chars[1] else set()
    palindromes = set()
    for i in range(len(chars) - 1):
        for j in range(i + 1, len(chars)):
            if chars[i] == chars[j]:
                palindrome = chars[i] + chars[j] + chars[i]
                palindromes.add(palindrome)
    return palindromes