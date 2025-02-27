def palindromes_between_indices(s):
    s = s[:3].lower()
    letters = [c for c in s if c.isalpha()]
    unique_letters = set(letters)
    if len(unique_letters) < 1:
        return set()
    elif len(unique_letters) == 1:
        palindrome = letters[0] * 3
        return {palindrome}
    else:
        palindromes = set()
        for c in unique_letters:
            for d in unique_letters:
                if c != d:
                    palindrome = c + d + c
                    palindromes.add(palindrome)
        return palindromes