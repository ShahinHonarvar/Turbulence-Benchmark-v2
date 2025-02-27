def palindromes_of_specific_lengths(s):
    sub_string = s[15:73]
    result = set()
    for length in range(19, 56):
        for i in range(len(sub_string) - length + 1):
            word = sub_string[i:i + length]
            if word == word.lower() and word == word[::-1].lower():
                result.add(word)
    return result