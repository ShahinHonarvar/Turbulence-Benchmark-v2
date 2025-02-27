def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[11:57]
    substring = substring.lower()
    for i in range(len(substring) - 19):
        current_substring = substring[i:i + 20]
        if current_substring == current_substring[::-1] and current_substring.isalpha():
            palindromes.add(current_substring)
        current_substring = substring[i:i + 21]
        if current_substring == current_substring[::-1] and current_substring.isalpha():
            palindromes.add(current_substring)
    return palindromes