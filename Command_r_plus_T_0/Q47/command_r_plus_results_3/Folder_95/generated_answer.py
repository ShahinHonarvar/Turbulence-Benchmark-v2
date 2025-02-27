def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[11:57]
    for i in range(len(substring) - 19):
        for j in range(3, 22):
            if j + i > len(substring):
                break
            temp_substring = substring[i:j + i]
            if temp_substring.lower() == temp_substring[::-1].lower():
                palindromes.add(temp_substring)
    return palindromes