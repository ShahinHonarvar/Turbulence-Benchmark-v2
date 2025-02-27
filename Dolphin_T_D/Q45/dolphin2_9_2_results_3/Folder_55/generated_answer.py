def palindromes_between_indices(s):
    if not s:
        return set()
    s = s[:3].lower()
    letters = set(s)
    length = len(s)
    palindromes = set()
    for i in range(length):
        for j in range(i + 1, length + 1):
            sub = s[i:j]
            if len(sub) >= 3 and all((letter in letters for letter in sub)):
                palindrome = sub + sub[::-1]
                palindromes.add(palindrome)
    return palindromes