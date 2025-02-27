def palindromes_between_indices(s):
    letters = [c for c in s[5:7].lower() if c.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for i in range(len(letters)):
            for j in range(i + 1, len(letters) + 1):
                substring = letters[i:j]
                for k in range(len(substring)):
                    first_part = substring[:k]
                    second_part = substring[k:]
                    if first_part == second_part[::-1]:
                        palindrome = ''.join(first_part + second_part)
                        palindromes.add(palindrome)
    return palindromes