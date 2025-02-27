def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[16:73].lower()
    palindromes = set()
    for i in range(len(substring) - 49):
        for j in range(2):
            current_substring = substring[i:i + 50 + j]
            if current_substring == current_substring[::-1] and current_substring.isalpha():
                palindromes.add(current_substring)
    return palindromes