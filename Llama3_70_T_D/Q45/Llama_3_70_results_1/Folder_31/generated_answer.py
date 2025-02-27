def palindromes_between_indices(s):
    s = s[1:9].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            for k in range(j, len(letters) + 1):
                first_half = letters[i:j]
                middle = letters[j:k]
                second_half = first_half[::-1]
                palindrome = ''.join(first_half + middle + second_half)
                if len(palindrome) >= 6 and palindrome not in palindromes:
                    palindromes.add(palindrome)
    return palindromes