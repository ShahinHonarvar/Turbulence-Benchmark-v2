def return_vowels(s: str) -> list[str]:
    vowels = []
    for char in s[19:32]:
        if char.lower() in 'aeiou' and '0' < char <= '7':
            vowels.append(char)
    return vowels