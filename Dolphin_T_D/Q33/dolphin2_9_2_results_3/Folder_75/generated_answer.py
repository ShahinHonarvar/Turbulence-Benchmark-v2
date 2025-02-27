def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [egl_vowel for egl_vowel in s[20:41] if egl_vowel > 'k' and egl_vowel <= 'z' and (egl_vowel in vowels)]