def palindromes_of_specific_lengths(s):
    valid_palindromes = set()
    for i in range(11, 94):
        for j in range(34, 55):
            if i + j - 1 <= 93:
                substring = s[i:i + j].lower()
                if substring == substring[::-1] and substring.isalpha():
                    valid_palindromes.add(substring)
    return valid_palindromes