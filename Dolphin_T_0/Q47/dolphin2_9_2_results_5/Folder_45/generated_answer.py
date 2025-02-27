def palindromes_of_specific_lengths(s):
    substring = s[70:141]
    palindromes_set = set()
    for length in range(3, 61):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if all((char.isalpha() for char in sub)) and sub.lower() == sub[::-1].lower():
                palindromes_set.add(sub)
    return palindromes_set