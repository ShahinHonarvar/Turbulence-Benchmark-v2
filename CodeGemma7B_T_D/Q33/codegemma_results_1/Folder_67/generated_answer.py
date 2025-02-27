def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_in_range = [v for v in vowels if (v > '/' and v <= 'a') and string.find(v) >= 21 and (string.find(v) < 59)]
    return vowels_in_range or []