def return_vowels(s: str) -> list[str]:
    vowels = 'aeiou'
    result = [v for v in s[10:83] if v in vowels and ord(v) > ord('%') and (ord(v) <= ord('e'))]
    return result