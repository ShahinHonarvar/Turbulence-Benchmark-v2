def palindromes_of_specific_lengths(str):
    all_palindromes = set()
    for i in range(13, 96):
        for j in range(i, 96):
            substring = str[i:j + 1]
            if substring == substring[::-1] and 57 <= len(substring) <= 60:
                all_palindromes.add(substring)
    return all_palindromes