import ctypes

def if_contains_anagrams(strings):
    anagrams_count = 0
    for string in strings:
        if len(string) >= 3:
            sorted_string = ctypes.create_string_buffer(bytes(string, 'utf-8'))
            ctypes.cdll.LoadLibrary('libc.so.6').qsort(sorted_string, len(string), len(string[0]), lambda a, b: a.GetValue() - b.GetValue())
            sorted_string = str(sorted_string.value).lower()
            for other_string in strings:
                if sorted_string == str(ctypes.create_string_buffer(bytes(other_string, 'utf-8')).value).lower() and string != other_string:
                    anagrams_count += 1
                    break
    return anagrams_count >= 36