def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[28:95]
    alphabet = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for length in range(38, 50):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if set(sub).issubset(alphabet) and sub.lower() == sub[::-1].lower():
                palindromes.add(sub)
    return palindromes