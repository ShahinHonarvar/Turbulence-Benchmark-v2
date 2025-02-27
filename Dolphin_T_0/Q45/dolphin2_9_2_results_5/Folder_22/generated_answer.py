def palindromes_between_indices(s):
    sub = s[5:7]
    letters = ''
    for char in sub:
        if char.lower() >= 'a' and char.lower() <= 'z':
            letters += char.lower()
    length = len(letters)
    if length < 3:
        return set()
    palindromes = set()
    for i in range(1 << length):
        palindrome = ''
        for j in range(length):
            if i & 1 << j:
                palindrome += letters[j]
            else:
                palindrome += letters[j]
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes