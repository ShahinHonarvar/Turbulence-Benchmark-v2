def palindromes_of_specific_lengths(string):
    substring = string[10:60]
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for length in range(18, 37):
        for i in range(len(substring) - length + 1):
            sub_sub = substring[i:i + length]
            lower_sub = ''.join((ch for ch in sub_sub if ch.lower() in english_letters))
            if len(lower_sub) == length and lower_sub == lower_sub[::-1]:
                palindromes.add(sub_sub)
    return palindromes