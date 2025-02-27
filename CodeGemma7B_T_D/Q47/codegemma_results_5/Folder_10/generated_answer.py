def palindromes_of_specific_lengths(str) -> set:
    result = set()
    for i in range(16, 60):
        for j in range(i + 16, 60):
            substring = str[i:j + 1]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring.lower())
    return result