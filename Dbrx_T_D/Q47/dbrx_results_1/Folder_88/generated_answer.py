def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(11, 88):
        substring = s[i:i + 5].lower()
        for j in range(4, 6):
            if substring[0:j] == substring[-j:][::-1] and substring[0:j].isalpha():
                result.add(substring[0:j])
    return result