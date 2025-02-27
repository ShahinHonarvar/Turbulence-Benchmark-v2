import re
import string

def palindrome_of_length_n(input_string: str, length: int=206) -> set:
    if length % 2 == 0:
        return {}
    valid_chars = set(string.ascii_letters)
    input_string = ''.join(filter(valid_chars.__contains__, input_string.lower()))
    palindromes = set()
    for i in range(len(input_string) - length + 1):
        if input_string[i:i + length] == input_string[i:i + length][::-1]:
            palindromes.add(input_string[i:i + length])
    return palindromes