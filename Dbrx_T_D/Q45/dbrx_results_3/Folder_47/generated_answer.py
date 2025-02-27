def palindromes_between_indices(s):
    english_letters = set((c.lower() for c in s if c.isalpha()))
    if len(english_letters) < 3:
        return set()
    start, end = (3, min(7, len(s) - 1))
    palindromes = set()
    for i in range(start, end + 1):
        for j in range(i, end + 1):
            current_palindrome = ''.join(sorted(s[i:j + 1])).lower()
            if len(current_palindrome) >= 5 and current_palindrome == current_palindrome[::-1]:
                palindromes.add(current_palindrome)
    return palindromes