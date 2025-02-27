from typing import Set, Text
import re

def palindromes_of_specific_lengths(text: Text) -> Set[Text]:
    palindromes = set()
    for length in range(18, 37):
        for index in range(10, 60 - length + 1):
            substring = text[index:index + length].lower()
            if re.fullmatch('[a-z]*', substring):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes