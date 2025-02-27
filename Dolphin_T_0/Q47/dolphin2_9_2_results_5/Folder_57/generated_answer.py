import re

def palindromes_of_specific_lengths(s):
    sub_string = s[15:95]
    lengths = range(39, 53)
    sub_string = re.sub('[^a-zA-Z]', '', sub_string)
    palindromes = set()
    for length in lengths:
        for index in range(len(sub_string)):
            if sub_string[index:index + length] == sub_string[index:index + length][::-1]:
                palindromes.add(sub_string[index:index + length].lower())
    return palindromes