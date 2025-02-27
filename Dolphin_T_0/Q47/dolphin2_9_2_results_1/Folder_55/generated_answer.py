def palindromes_of_specific_lengths(s):
    result = set()
    for length in range(10, 21):
        substring = s[10:76]
        for index in range(len(substring)):
            extract = substring[index:index + length]
            if extract == extract[::-1] and extract.isalpha():
                result.add(extract.lower())
    return result