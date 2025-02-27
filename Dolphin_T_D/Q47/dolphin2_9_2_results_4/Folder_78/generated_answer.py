def palindromes_of_specific_lengths(s):
    substring = s[15:73]
    palindromes = set()
    for length in range(19, 56):
        for start_index in range(len(substring) - length + 1):
            sub_word = substring[start_index:start_index + length]
            if sub_word.lower() == sub_word[::-1].lower():
                palindromes.add(sub_word)
    return palindromes