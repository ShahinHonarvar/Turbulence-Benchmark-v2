def palindromes_of_specific_lengths(s):
    substring = s[45:99].lower()
    length_range = range(40, 48)
    palindromes = set()
    for length in length_range:
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes