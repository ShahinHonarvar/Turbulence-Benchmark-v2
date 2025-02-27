def return_vowels(s: str) -> list:
    vowels = []
    for char in s:
        if 32 <= ord(char) < 97 and 'Q' < char <= ']':
            if char.lower() in 'aeiou':
                vowels.append(char)
    return vowels