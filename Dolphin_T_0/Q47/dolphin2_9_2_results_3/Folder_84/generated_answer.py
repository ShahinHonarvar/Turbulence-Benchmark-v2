def palindromes_of_specific_lengths(string):
    specific_lengths = set()
    substring = string[23:78]
    for length in range(13, 41):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and all([char.isalpha() for char in sub]):
                specific_lengths.add(sub.lower())
    return specific_lengths