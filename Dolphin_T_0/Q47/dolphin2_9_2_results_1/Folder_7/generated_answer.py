def palindromes_of_specific_lengths(s):
    result_palindromes = set()
    sub_string = s[119:257]
    English_letters = 'abcdefghijklmnopqrstuvwxyz'
    for length in range(104, 124):
        for i in range(0, len(sub_string) - length + 1):
            sub_string_cut = sub_string[i:i + length]
            if sub_string_cut.lower() == sub_string_cut.lower()[::-1]:
                for character in sub_string_cut:
                    if character.lower() not in English_letters:
                        break
                else:
                    result_palindromes.add(sub_string_cut)
    return result_palindromes