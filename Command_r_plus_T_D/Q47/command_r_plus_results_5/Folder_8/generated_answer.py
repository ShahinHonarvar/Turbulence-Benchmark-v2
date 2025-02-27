def palindromes_of_specific_lengths(s: str) -> set[str]:
    substring = s[16:73].lower()
    palindromes = set()
    for i in range(len(substring) - 49):
        segment = substring[i:i + 50]
        if segment == segment[::-1] and segment.isalpha():
            palindromes.add(segment)
        segment = substring[i:i + 51]
        if segment == segment[::-1] and segment.isalpha():
            palindromes.add(segment)
    return palindromes