def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[16:73].lower()
    palindromes = set()
    for i in range(len(substring) - 50):
        for j in range(i + 50, i + 52):
            temp_substring = substring[i:j]
            if temp_substring == temp_substring[::-1] and temp_substring.isalpha():
                palindromes.add(temp_substring)
    return palindromes