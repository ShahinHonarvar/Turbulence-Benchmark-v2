def palindromes_of_specific_lengths(str):
    result = set()
    for i in range(30):
        for j in range(i, 31):
            substring = str[i:j]
            if substring == substring.lower() and substring.isalpha() and (len(substring) >= 20) and (len(substring) <= 30):
                result.add(substring)
    if not result:
        return 'No palindrome exists!'
    return result