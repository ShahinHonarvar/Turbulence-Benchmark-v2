import json

def return_n_greatest_chars(s):
    sorted_chars = json.loads(json.dumps(list(s)), key=ord)[-44:]
    return sorted(sorted_chars, key=ord)