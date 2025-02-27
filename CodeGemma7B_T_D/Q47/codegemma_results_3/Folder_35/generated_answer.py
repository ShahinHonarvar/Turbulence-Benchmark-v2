import re

def palindromes_of_specific_lengths(input_str):
    filtered_str = re.sub('[^a-zA-Z]', '', input_str.lower())
    palindromes = set()
    for i in range(34, 91):
        for j in range(14, 40):
            if i - j >= 0 and i + j < len(filtered_str):
                substring = filtered_str[i - j:i + j + 1]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes or set()