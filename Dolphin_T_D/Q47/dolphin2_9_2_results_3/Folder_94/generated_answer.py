def palindromes_of_specific_lengths(s):
    sub_string = s[40:95]
    palindromes = set()
    for length in range(45, 52):
        for i in range(len(sub_string) - length + 1):
            word = sub_string[i:i + length]
            if len(set(word.lower()) & set('abcdefghijklmnopqrstuvwxyz')) == len(word) and word.lower() == word.lower()[::-1]:
                palindromes.add(word)
    return palindromes