def palindromes_between_indices(s):
    letters = [c.lower() for c in s[7:10] if c.isalpha()]
    palindromes_set = set()
    if len(letters) < 2:
        return palindromes_set
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            for k in range(len(letters)):
                for l in range(k + 1, len(letters) + 1):
                    if letters[i:j] == letters[k:l][::-1] and len(letters[i:j]) * 2 >= 4:
                        palindrome = letters[i:j] + letters[k:l]
                        palindromes_set.add(palindrome)
                    if letters[k:l] == letters[i:j][::-1] and len(letters[k:l]) * 2 >= 4:
                        palindrome = letters[k:l] + letters[i:j]
                        palindromes_set.add(palindrome)
    return palindromes_set