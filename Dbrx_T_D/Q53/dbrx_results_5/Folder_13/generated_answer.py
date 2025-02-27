import re
from typing import Set

def palindrome_of_length_at_least_n(input_string: str) -> Set[str]:
    input_string = input_string.lower()
    palindromes = set()
    for n in range(52, 0, -1):
        for i in range(len(input_string) - n + 1):
            if i - n - 1 >= 0 and input_string[i - n - 1:i] == input_string[i:i + n] and (input_string[i - n - 1] != ' '):
                palindromes.add(input_string[i - n - 1:i + n][::-1])
            if re.match('^[a-zA-Z]*$', input_string[i:i + n]) and input_string[i:i + n] == input_string[i:i + n][::-1]:
                palindromes.add(input_string[i:i + n])
    return palindromes