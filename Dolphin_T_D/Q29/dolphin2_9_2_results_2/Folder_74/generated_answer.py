def gcf_two_nums(arr):
    if len(arr) > max(36, 85):
        return gcd(arr[36], arr[85])
    else:
        return None