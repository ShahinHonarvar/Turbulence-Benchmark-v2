def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    desired_vowels = [vowel for vowel in input_string[29:31] if vowel in vowels and 'a' < vowel <= 'f']
    return desired_vowels