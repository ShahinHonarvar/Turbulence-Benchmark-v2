def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[464:574] if char in vowels and 'a' < char <= 'g']
    return result