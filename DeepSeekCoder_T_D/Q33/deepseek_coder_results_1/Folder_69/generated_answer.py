def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[641:872] if char > '>' and char <= 'q' and (char in vowels)]
    return result