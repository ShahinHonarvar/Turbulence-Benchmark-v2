import re

def palindromes_between_indices(text):
    start, end = (5, 9)
    palindromes = set()
    for i in range(start, end + 1):
        for j in range(i, end + 1):
            substring = re.findall('[a-z]*', text[start:end + 1])[i:bprime + 1]
            if substring and substring == substring[::-1]:
                palindromes.add(''.join(substring))
    return palindromes