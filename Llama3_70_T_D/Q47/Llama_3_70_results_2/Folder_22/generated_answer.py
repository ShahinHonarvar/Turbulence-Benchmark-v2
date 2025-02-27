def palindromes_of_specific_lengths(string):
    substring = string[100:201].lower()
    result = set()
    for length in range(5, 11):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.isalpha() and sub == sub[::-1]:
                result.add(sub)
    return result