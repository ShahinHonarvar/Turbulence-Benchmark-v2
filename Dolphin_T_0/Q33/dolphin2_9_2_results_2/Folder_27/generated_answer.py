def return_vowels(in_str):
    vowels = ['a', 'e', 'i', 'o']
    sub_str = in_str[29:31]
    result = [c for c in sub_str if c in vowels and 'a' < c <= 'f']
    return result