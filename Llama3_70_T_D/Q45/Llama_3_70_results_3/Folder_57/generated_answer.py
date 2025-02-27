def palindromes_between_indices(s):
    s = s.lower()
    substring = s[2:6]
    letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for l in range(k + 1, len(letters)):
                    for m in range(l + 1, len(letters)):
                        palindrome = letters[i] + letters[j] + letters[k] + letters[l] + letters[m] + letters[l] + letters[k] + letters[j] + letters[i]
                        palindromes.add(palindrome)
    return palindromes