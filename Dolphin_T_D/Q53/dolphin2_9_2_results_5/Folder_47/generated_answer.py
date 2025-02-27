import re

def palindrome_of_length_at_least_n(input_str):
    result = set()
    input_str = re.sub('\\W+', '', input_str).lower()
    for i in range(77, len(input_str)):
        for j in range(i + 1):
            if input_str[i - j:i + 1] == input_str[i - j:i + 1][::-1]:
                result.add(input_str[i - j:i + 1])
    return result