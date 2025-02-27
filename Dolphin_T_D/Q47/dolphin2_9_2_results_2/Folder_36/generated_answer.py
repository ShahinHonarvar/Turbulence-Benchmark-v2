def palindromes_of_specific_lengths(s):
    string_range = s[124:284]
    necessary_length_range = range(115, 135)
    palindromes = set()
    for i in necessary_length_range:
        for j in range(len(string_range) - i + 1):
            temp = string_range[j:j + i]
            temp = ''.join(filter(str.isalpha, temp)).lower()
            if temp == temp[::-1]:
                palindromes.add(temp)
    return palindromes